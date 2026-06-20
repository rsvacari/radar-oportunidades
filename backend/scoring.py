def _to_float_safe(value):
    try:
        value = value.replace('.', '').replace(',', '.')
        return float(value)
    except:
        return None

def score_acao(row):
    pl = _to_float_safe(row.get("P/L", ""))
    pvp = _to_float_safe(row.get("P/VP", ""))
    roe = _to_float_safe(row.get("ROE", ""))
    dy = _to_float_safe(row.get("Div.Yield", ""))

    score = 0

    if pl is not None:
        if pl > 0 and pl < 10: score += 3
        elif pl <= 15: score += 2
        elif pl <= 20: score += 1

    if pvp is not None:
        if pvp < 1: score += 3
        elif pvp <= 1.5: score += 2
        elif pvp <= 2: score += 1

    if roe is not None:
        if roe >= 20: score += 3
        elif roe >= 15: score += 2
        elif roe >= 10: score += 1

    if dy is not None:
        if dy >= 8: score += 3
        elif dy >= 5: score += 2
        elif dy >= 3: score += 1

    return score

def score_fii(row):
    dy = _to_float_safe(row.get("Div.Yield", ""))
    pvp = _to_float_safe(row.get("P/VP", ""))

    score = 0

    if dy is not None:
        if dy >= 10: score += 3
        elif dy >= 8: score += 2
        elif dy >= 6: score += 1

    if pvp is not None:
        if pvp < 0.9: score += 3
        elif pvp <= 1.0: score += 2
        elif pvp <= 1.1: score += 1

    return score

def rank_acoes(df):
    df = df.copy()
    df["score"] = df.apply(score_acao, axis=1)
    return df.sort_values("score", ascending=False)

def rank_fiis(df):
    df = df.copy()
    df["score"] = df.apply(score_fii, axis=1)
    return df.sort_values("score", ascending=False)
