import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler, Normalizer
from sklearn.model_selection import GridSearchCV


class dataloader:
    def __init__(self):
        dataset = pd.read_csv('../data/incident_gas_distribution_jan2010_present.csv')

        X = dataset[['COMMODITY_RELEASED_TYPE', 'ACCIDENT_IDENTIFIER','FLOW_CONT_KEY_CRIT_IND', 'FLOW_CONT_MAIN_VALVE_IND','FLOW_CONT_SERVICE_VALVE_IND','FLOW_CONT_METER_REG_IND','FLOW_CONT_EXCESS_FLOW_IND','FLOW_CONT_SQUEEZE_OFF_IND','FLOW_CONT_STOPPLE_FITNG_IND','IGNITE_IND','EXPLODE_IND','FEDERAL','LOCATION_TYPE','INCIDENT_AREA_TYPE','CROSSING','PIPE_FACILITY_TYPE','MATERIAL_INVOLVED','RELEASE_TYPE','EMPLOYEE_DRUG_TEST_IND','CONTRACTOR_DRUG_TEST_IND','INTERNAL_EXTERNAL','NATURAL_FORCE_TYPE','OUTSIDE_FORCE_TYPE']]

        Y = dataset[['FATAL','INJURE']]

        cost=dataset[['EST_COST_OPER_PAID','EST_COST_PROP_DAMAGE','EST_COST_EMERGENCY','EST_COST_OTHER','EST_COST_OTHER_DETAILS','GAS_COST_IN_MCF','EST_COST_UNINTENTIONAL_RELEASE','EST_COST_INTENTIONAL_RELEASE']]
        cost.replace(np.nan, 0)
        Y['TOTAL_COST'] = dataset.sum(axis=1)
        X[['FLOW_CONT_SERVICE_VALVE_IND','FLOW_CONT_KEY_CRIT_IND','FLOW_CONT_MAIN_VALVE_IND','FLOW_CONT_METER_REG_IND','FLOW_CONT_EXCESS_FLOW_IND','FLOW_CONT_STOPPLE_FITNG_IND','EXPLODE_IND']]=X[['FLOW_CONT_SERVICE_VALVE_IND','FLOW_CONT_KEY_CRIT_IND','FLOW_CONT_MAIN_VALVE_IND','FLOW_CONT_METER_REG_IND','FLOW_CONT_EXCESS_FLOW_IND','FLOW_CONT_STOPPLE_FITNG_IND','EXPLODE_IND']].replace(np.nan,'NO')


        X['COMMODITY_RELEASED_TYPE']=X['COMMODITY_RELEASED_TYPE'].replace(np.nan,'OTHER GAS')

        X['FLOW_CONT_SQUEEZE_OFF_IND']=X['FLOW_CONT_SQUEEZE_OFF_IND'].replace(np.nan,'NO')

        X['INTERNAL_EXTERNAL']=X['INTERNAL_EXTERNAL'].replace(np.nan,'INTERNAL CORROSION')

        X['NATURAL_FORCE_TYPE']=X['NATURAL_FORCE_TYPE'].replace(np.nan,'OTHER NATURAL FORCE DAMAGE')

        X['OUTSIDE_FORCE_TYPE']=X['OUTSIDE_FORCE_TYPE'].replace(np.nan,'OTHER OUTSIDE FORCE DAMAGE')

        X_transform =  pd.get_dummies(X, drop_first=True)

        scaler = StandardScaler()
        # scaler.fit(np.array(Y['TOTAL_COST']).reshape((-1,1)))
        # Y['TOTAL_COST']= scaler.transform(np.array(Y['TOTAL_COST']).reshape((-1,1)))

        Y['INJURE_BOOL'] = [0 if val== 0 else 1 for val in Y['INJURE']]
        Y['FATAL_BOOL'] = [0 if val== 0 else 1 for val in Y['FATAL']]
        Y=Y.drop(columns = ['FATAL', 'INJURE'], axis=1 )



        lig = np.log(Y['TOTAL_COST'])
        Y_cost_binary = lig>16.83

        scaler.fit(np.array(Y['TOTAL_COST']).reshape(-1,1))
        Y['TOTAL_COST']= Y_cost_binary
        Y['TOTAL_COST'] = Y['TOTAL_COST'].map(lambda x: 1 if x==True else 0)

        y = pd.DataFrame(Y, columns=['TOTAL_COST','INJURE_BOOL','FATAL_BOOL'])
        self.X = X_transform
        self.y= y



