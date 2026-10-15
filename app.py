import math
from decimal import Decimal, ROUND_HALF_UP

import streamlit as st

st.set_page_config(page_title="Жақын квадрат әдісі", page_icon="√", layout="centered")
st.title("Жақын квадрат әдісін тексеру")
st.write("a санын енгізіңіз. Бағдарлама жақын толық квадратты таңдап, формуламен шыққан нәтижені нақты квадрат түбірмен салыстырады.")


def round_half_up(value: float, places: int) -> Decimal:
    quantum = Decimal("1").scaleb(-places)
    return Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_UP)


def nearest_square(a: float) -> int:
    lower_root = math.isqrt(math.floor(a))
    candidates = tuple(x for x in (lower_root**2, (lower_root + 1) ** 2) if x > 0)
    return min(candidates, key=lambda square: abs(a - square))


a = st.number_input("a саны (a ≥ 0)", min_value=0.0, value=101.0, step=1.0, format="%.10g")
places = st.selectbox("Дөңгелектеу дәлдігі", [0, 1, 2, 3], index=1, format_func=lambda n: {0: "Бүтінге дейін", 1: "Ондық үлеске дейін", 2: "Жүздік үлеске дейін", 3: "Мыңдық үлеске дейін"}[n])

if a == 0:
    st.success("√0 = 0. Нәтиже дұрыс.")
else:
    b = nearest_square(a)
    sqrt_b = math.sqrt(b)
    approx = (a + b) / (2 * sqrt_b)
    exact = math.sqrt(a)
    app_rounded = round_half_up(approx, places)
    exact_rounded = round_half_up(exact, places)

    st.subheader("Есептеу")
    st.latex(rf"b={b}={sqrt_b:g}^2")
    st.latex(rf"\sqrt{{{a:g}}}\approx\frac{{{a:g}+{b}}}{{2\sqrt{{{b}}}}}={approx:.12g}")
    st.write(f"**Формула бойынша жуық мән:** {approx:.12g}")
    st.write(f"**Нақты квадрат түбірі:** √{a:g} = {exact:.12g}")
    st.write(f"**Абсолют қате:** {abs(approx - exact):.12g}")
    st.write(f"**Формула мәнін дөңгелектегенде:** {app_rounded}  ")
    st.write(f"**Нақты мәнді дөңгелектегенде:** {exact_rounded}")
    if app_rounded == exact_rounded:
        st.success("Дөңгелектелген жауап нақты мәнмен сәйкес келеді.")
    else:
        st.warning("Жуық мәнді дөңгелектеу нақты квадрат түбірдің дөңгелектелген мәнінен өзгеше. Нақты мәнді басшылыққа алыңыз.")

with st.expander("Әдіс туралы"):
    st.markdown("""
Формула: `√a ≈ (a + b) / (2√b)`, мұндағы `b` — `a` санына ең жақын толық квадрат.

Бұл жуықтау болғандықтан, соңғы жауапты дөңгелектемес бұрын нақты квадрат түбірмен салыстыру қажет.
""")
st.caption("Есептеу серверде сақталмайды; қолданба тек енгізілген санды есептейді.")
