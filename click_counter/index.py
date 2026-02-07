from browser import document

score_value = 0

def increase(ev):
    global score_value
    score_value += 1
    document['score'].text = f"{score_value}"

def decrease(ev):
    global score_value
    score_value -= 1
    rules()
    document['score'].text = f"{score_value}"

def reset(ev):
    global score_value
    score_value = 0
    document['score'].text = f"{score_value}"

def rules():
    global score_value
    if score_value < 0:
        score_value = 0
    return

document['increase'].bind('click', increase)
document['decrease'].bind('click', decrease)
document['reset'].bind('click', reset)
