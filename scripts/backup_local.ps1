# Copia os ficheiros de trabalho que ficam fora do Git (listados em .git/info/exclude)
# para <Destino>\<data-hora>\ em cada destino, mantendo a estrutura de pastas.
# Em cada destino ficam só as $Manter cópias mais recentes.
# Uso: powershell -ExecutionPolicy Bypass -File scripts\backup_local.ps1 [-Destinos <pasta1>,<pasta2>] [-Manter 15]
param(
    [string[]]$Destinos = @("D:\SCHOOL\_backup_biomat", "C:\Users\aomas\OneDrive\_backup_biomat"),
    [int]$Manter = 15
)
$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $PSScriptRoot
$exclude = Join-Path $repo ".git\info\exclude"
$carimbo = Get-Date -Format "yyyy-MM-dd_HHmmss"
$formato = '^\d{4}-\d{2}-\d{2}_\d{6}$'  # só as pastas criadas por este script

$ficheiros = @(git -C $repo -c core.quotepath=off ls-files --others --ignored --exclude-from="$exclude")
if ($ficheiros.Count -eq 0) {
    Write-Host "Nada para copiar."
    exit 0
}

foreach ($destino in $Destinos) {
    $pasta = Join-Path $destino $carimbo
    foreach ($f in $ficheiros) {
        $alvo = Join-Path $pasta $f
        New-Item -ItemType Directory -Force (Split-Path -Parent $alvo) | Out-Null
        Copy-Item -LiteralPath (Join-Path $repo $f) -Destination $alvo
    }
    $copiados = @(Get-ChildItem -LiteralPath $pasta -Recurse -File).Count

    # Nomes aaaa-mm-dd_hhmmss ordenam-se cronologicamente; apaga as mais antigas além de $Manter.
    $antigas = @(Get-ChildItem -LiteralPath $destino -Directory |
        Where-Object { $_.Name -match $formato } |
        Sort-Object Name -Descending |
        Select-Object -Skip $Manter)
    foreach ($a in $antigas) { Remove-Item -LiteralPath $a.FullName -Recurse -Force }

    Write-Host "$copiados ficheiros copiados para $pasta ($($antigas.Count) cópias antigas apagadas)"
}
