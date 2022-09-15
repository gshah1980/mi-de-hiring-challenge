import pandas as pd


def get_customers():
    # Return customer table as a pandas data frame
    df = pd.read_csv('customer_table.csv')

    return df


def get_email_to_customer_cross_reference():
    # Return email address to customer id cross-reference table as a pandas data frame
    df = pd.read_csv('xref_table.csv')

    return df


def get_transaction_log():
    # Return transactions log as a pandas data frame
    df = pd.read_csv('transaction_table.csv')

    return df


def objective_one():
    """
    Objective One:
    Return the average revenue per transaction using all data in transaction log.
    """
    df = get_transaction_log()
    result = df.groupby('customer_id')['revenue'].mean()

    return result



def objective_two():
    """
    Objective Two:
    Return the total revenue from customers who are opted-in to email and are
    subscribed to the loyalty program.
    """
    dft = get_transaction_log()
    dfc = get_customers()
    dfe = get_email_to_customer_cross_reference()
    
    result =  groupby(query(pd.merge(pd.merge(dft, dfe, how='inner', on = 'customer_id'),dfc, how='inner', on = 'email_address')loyalty_status=='true'&&opt_in_status=='true')'customer_id')['revenue'])sum()
    return result



# Do not edit below this line ------------------------
print('The average revenue per transaction is ${}.'.format(objective_one()))
print('The total revenue from opted-in loyalty customers is ${}.'.format(objective_two()))
