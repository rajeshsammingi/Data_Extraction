import streamlit as st
from Data_Ingestion import reading as rd
from Data_Ingestion import profiling as pg
from Data_Ingestion import writing as wt

def main(config_path):
    """
    Main function to process data based on configuration file.
    
    Args:
        config_path (str): Path to the configuration CSV file.
    """
    try:
        config_df = rd.read_from_csv_file(config_path)

        for i in range(len(config_df)-1):
            input_path = config_df.at[i, 'input_path']
            file_format = config_df.at[i, 'file_format']
            file_name = config_df.at[i, 'file_name']
            df = rd.read_data_from_file(file_format, input_path)
            
            output_path = config_df.at[len(config_df) - 1, 'input_path']
            wt.write_to_csv(output_path, df, file_name)
            df = pg.data_profiling(df, file_name)
            if st.button(file_name):
                st.write(df)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

config_path = st.file_uploader("Choose config file", type="csv")
if config_path is not None:
    main(config_path)




# import sys
# sys.path.append("/home/razz/Rajesh/Data_Ingestion/Data_Ingestion")

# import reading as rd
# import profiling as pg
# import streamlit as st 
# import writing as wt

# def main(config_path):
#     config_df = rd.read_from_csv_file(config_path)

#     input_iterates = len(config_df)
#     for i in range(input_iterates-1):
#         input_path = config_df.at[i,'input_path']
#         file_format = config_df.at[i,'file_format']
#         file_name = config_df.at[i,'file_name']
#         df = rd.read_data_from_file(file_format,input_path)
        
#         output_path = config_df.at[input_iterates-1,'input_path']
#         wt.write_to_csv(output_path,df,file_name)
#         df = pg.data_profiling(df,file_name)
#         if st.button(file_name):
#             st.write(df)
    

# config_path = st.file_uploader("choose config file", type="csv")
# if config_path is not None:
#     main(config_path)



