{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Executable SSH Research Workflow\
\
This project demonstrates an executable RO-Crate for computational SSH research.\
\
## Components\
\
- Input dataset (`data/speeches.csv`)\
- Python workflow (`src/analyze.py`)\
- Jupyter notebook (`notebooks/analysis.ipynb`)\
- Execution environment (`environment.yml`)\
- CodeMeta metadata (`codemeta.json`)\
- SSH vocabulary (`vocab/vocab.ttl`)\
- Output dataset (`outputs/word_counts.csv`)\
- Execution provenance log (`logs/execution_log.json`)\
\
## Running the workflow\
\
Activate the environment:\
\
```bash\
cd ~/Desktop/rocrate\
source .venv/bin/activate}