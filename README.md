# Heart Rate vs. Temperature Analysis — 6-Month Longitudinal Study

A data engineering and pattern detection project investigating whether 
ambient temperature changes trigger measurable cardiovascular responses 
in real-world conditions. Built using Apple Watch physiological data fused 
with OpenWeatherMap API environmental feeds across 6 participants over 6 months.

---

## The Question

Do temperature drops cause heart rate changes — and if so, under what 
conditions and for which individuals?

Most studies on this topic use controlled lab environments. This project 
used real-world data: people going about their lives, wearing Apple Watches, 
in Hyderabad across varying seasonal conditions.

---

## Tech Stack

- **Python 3** — Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Apple HealthKit XML** — Heart rate data exported from Apple Watch 
  (5–10 min intervals)
- **OpenWeatherMap API** — Hourly historical temperature data
- **Statistical Methods** — Pearson correlation, linear & multiple 
  regression, ANOVA, paired T-tests, time-lagged correlation
- **ML Models** — Random Forest regression, ARIMA time series

---

## Data Pipeline
Apple Watch XML → XML Parser → Cleaned HR DataFrame
↓
OpenWeatherMap API → Hourly Temp Feed → Temporal Alignment
↓
Combined Dataset (combined.xlsx)
↓
Contextual Classification → Analysis Layer

**Contextual classification framework:**
Each data point was tagged across three dimensions before analysis:

| Dimension | Categories |
|---|---|
| Location | Indoor / Outdoor |
| Time of Day | Morning / Afternoon / Evening / Night |
| Activity State | Rest / Active |

This isolation step was critical — without it, confounding variables 
(exercise, sleep) would have masked any temperature signal entirely.

---

## Key Findings

**At the population level:** Weak to no correlation between temperature 
drops and immediate heart rate changes. Random Forest models showed low 
predictive power, confirming temperature alone is not a reliable HR predictor.

**At the individual level:** P3 showed a consistently strong positive 
cardiovascular response to cold exposure — statistically significant 
across multiple methods. This outlier finding suggests individual 
physiological sensitivity varies far more than population averages indicate.

**Contextual patterns:** Heart rate responses to temperature were most 
visible during nighttime, rest periods, and outdoor exposure. Active 
daytime periods produced too much confounding signal to isolate 
temperature effects.

**Honest conclusion:** The null result at population level is the 
finding. Consumer-grade wearables can capture individual variability 
meaningfully, but are not reliable for population-level environmental 
health monitoring without individual calibration.

---

## Methodology

1. **Data Collection** — Apple Watch HR exports (XML) + OpenWeatherMap 
   API historical pulls for 6 participants across 6 months
2. **Preprocessing** — Temporal alignment of 5–10 min HR intervals to 
   hourly temperature feeds, noise filtering, outlier flagging
3. **Contextual Classification** — Each observation tagged by location 
   type, time of day, and activity state to isolate confounding variables
4. **Statistical Analysis** — Pearson correlation, linear regression, 
   multiple regression, time-lagged correlation, ANOVA, paired T-tests
5. **Time Series Modelling** — ARIMA models per participant to detect 
   lagged physiological responses
6. **Machine Learning** — Random Forest regression to test predictive 
   power of temperature features on HR outcomes

---

## Repository Structure
├── Main code.py                  # Full analysis pipeline
├── changing the xml files.py     # HealthKit XML parser
├── combined.xlsx                 # Processed dataset
├── requirements.txt
├── README.md
└── Analysing the Relationship... # Full dissertation (.docx)

---

## How to Run

```bash
git clone https://github.com/crazyandiee/Heart-Rate-vs.-Temperature-Analysis.git
cd Heart-Rate-vs.-Temperature-Analysis
pip install -r requirements.txt
python "Main code.py"
```

---

## Research Questions

1. Do temperature drops trigger significant heart rate changes at the 
   population level?
2. Are there cold exposure thresholds that produce stronger physiological 
   responses?
3. How much does individual variation (fitness, environment, sensitivity) 
   affect results?
4. Can consumer-grade wearables support population-level health monitoring?

---

## Full Report

The complete dissertation is in the repository root — includes literature 
review, full methodology, statistical outputs, visualisations, and 
limitations analysis.
