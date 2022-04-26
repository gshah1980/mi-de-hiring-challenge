# Data Engineer, Client Solutions - Hiring Challenge

In this test, you’ll need to retrieve a series of data files, decrypt them, then perform some basic aggregations on them using python and pandas. The data files contain mocked data supporting a fictitious company’s email program.

More detailed information is below.

- Three files containing comma-separated data are provided:

  - `transaction_table.csv.pgp`

    This is a transaction log. Each row represents a consumer purchase and includes the customer id, date, and the revenue associated with the purchase.

  - `customer_table.csv.pgp`

    This is an email opt-ins table. Each row contains an email address along with various attributes (a boolean representing their membership in the loyalty program, a boolean representing their opt-in status for receiving email, and a language preference).

  - `xref_table.csv.pgp`

    This is a cross-reference table mapping customer ids to email addresses.

- The files are hosted on an SFTP server:

  - Hostname: `sftp.company.com`
  - Username: `miuser`
  - Password: `mipassword`

- The data files are PGP encrypted using GnuPG 2.3.4. The private key needed to decrypt these files is also provided on the SFTP server with filename `pgpkey`.

- Once the data is obtained and decrypted, use the `code_starter.py` file to begin coding data aggregation to meet the following two objectives:
  - Objective One: Compute the average revenue per transaction using all data in transaction log.
  - Objective Two: Compute the total revenue from customers who are opted-in to email and are subscribed to the loyalty program.
  - Both objectives above should result in a numeric answers when executing the code. Provide those two answers to the Movable Ink recruiter along with your completed code file.
