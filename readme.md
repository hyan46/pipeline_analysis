Welcome to the Pipeline Analysis repository. This project provides tools and scripts for analyzing pipeline data, focusing on preprocessing, feature extraction, model training, and evaluation, particularly with datasets from HIAD and PHMSA.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
  - [HIAD Data](#hiad-data)
  - [PHMSA Data](#phmsa-data)
  - [PHMSA Risk Analysis](#phmsa-risk-analysis)
  - [PHMSA Text Analysis](#phmsa-text-analysis)
- [Usage](#usage)
  - [Preprocessing](#preprocessing)
  - [Feature Extraction](#feature-extraction)
  - [Model Training](#model-training)
  - [Model Evaluation](#model-evaluation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

Clone the repository and install the required dependencies.

\`\`\`bash
git clone https://github.com/hyan46/pipeline_analysis.git
cd pipeline_analysis
pip install -r requirements.txt
\`\`\`

## Project Structure

The repository is organized as follows:

\`\`\`
pipeline_analysis/
│
├── HIAD/
│   └── data/
│       └── JRC HIAD 2.0 export 2022 01 01 for users.xlsx   # Raw HIAD dataset
│
├── PHMSA/
│   ├── data/
│   │   ├── incident_gas_distribution_1970_mid1984.csv      # Raw PHMSA data
│   │   ├── incident_gas_distribution_jan2010_present.csv   # Raw PHMSA data
│   │   ├── incident_gas_distribution_mar2004_dec2009.csv   # Raw PHMSA data
│   │   └── incident_gas_distribution_mid1984_feb2004.csv   # Raw PHMSA data
│   ├── risk_analysis/
│   │   ├── ML_Final_Portfolio.ipynb                        # Notebook for final ML portfolio
│   │   ├── incident_gas_distribution_Project_ML.ipynb      # Notebook for ML project
│   │   ├── preprocessing.py                                # Script for data preprocessing
│   │   └── risk_analysis.ipynb                             # Notebook for risk analysis
│   └── text_analysis/
│       └── Text_Mining.ipynb                               # Notebook for text mining
│
├── requirements.txt                                        # Required dependencies
├── LICENSE                                                 # License for the project
└── README.md                                               # Readme file with project information
\`\`\`

### HIAD Data

- **Directory:** `HIAD/data/`
  - **JRC HIAD 2.0 export 2022 01 01 for users.xlsx**: Raw HIAD dataset.

### PHMSA Data

- **Directory:** `PHMSA/data/`
  - **incident_gas_distribution_1970_mid1984.csv**: Raw PHMSA data.
  - **incident_gas_distribution_jan2010_present.csv**: Raw PHMSA data.
  - **incident_gas_distribution_mar2004_dec2009.csv**: Raw PHMSA data.
  - **incident_gas_distribution_mid1984_feb2004.csv**: Raw PHMSA data.

### PHMSA Risk Analysis

- **Directory:** `PHMSA/risk_analysis/`
  - **ML_Final_Portfolio.ipynb**: Jupyter notebook for final machine learning portfolio.
  - **incident_gas_distribution_Project_ML.ipynb**: Jupyter notebook for ML project.
  - **preprocessing.py**: Script for data preprocessing.
  - **risk_analysis.ipynb**: Jupyter notebook for risk analysis.

### PHMSA Text Analysis

- **Directory:** `PHMSA/text_analysis/`
  - **Text_Mining.ipynb**: Jupyter notebook for text mining.

