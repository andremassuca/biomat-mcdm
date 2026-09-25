"""Fase 1 — triagem por critérios estritos (passa/falha)."""
from __future__ import annotations
import pandas as pd


def apply_strict(materials: pd.DataFrame, rules: dict[str, tuple[str, float]]) -> pd.DataFrame:
    """Remove alternativas que falham qualquer regra estrita.

    rules: {propriedade: (operador, limite)}, operador em {">=", "<=", "=="}
    Ex.: {"Segurança iónica / risco ALTR (ordinal 1-5)": (">=", 2)}  → elimina o MoM.

    Devolve o DataFrame só com as alternativas aprovadas e regista (print/log)
    quais foram eliminadas e porquê — isto vai para o relatório.
    """
    raise NotImplementedError
