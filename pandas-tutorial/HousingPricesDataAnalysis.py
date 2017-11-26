import pandas as pd
import os
import quandl
import pickle

# Setting Pandas display options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

states_wiki_url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states'
current_path = os.path.dirname(os.path.realpath(__file__))
api_key_file_path = os.path.join(current_path, "../data/quandl_api_key.txt")
pickled_file = os.path.join(current_path, "../data/states.pickle")
api_key = open(api_key_file_path, 'rb').read()


# get a list of all the us states in abbreviated form
def get_states_list():
    df = pd.read_html(states_wiki_url)
    return df[0][0][1:]


# Download Housing Prices data for all states and save it into states.pickle
def grab_initial_state_data():
    main_df = pd.DataFrame()
    for state in get_states_list():
        query = "FMAC/HPI_" + str(state)
        df = quandl.get(query, authtoken=api_key).rename(columns={'Value': state})
        if main_df.empty:
            main_df = df

        else:
            main_df = main_df.join(df)
    '''
    main_df.to_pickle('states.pickle')
    pd.read_pickle('states.pickle')
    '''
    pickle_out = open(pickled_file, 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


# grab_initial_state_data()

def load_saved_data():
    pickled_input = open(pickled_file, 'rb')
    housing_prices_data = pickle.load(pickled_input)
    print (housing_prices_data.head())


load_saved_data()
