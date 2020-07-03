# coding=utf-8
import pandas
import csv

# export from Pecunia (in that order)
columns = [
    'Valuta', # 'Valutadatum' 
    'Datum', # 'Buchungsdatum'
    'Amount', # 'Wert'
    'Balance', # 'Saldo'
    'Counter Account Owner', # 'Empfänger'
    'Customer Reference', # 'Kundenreferenz'
    'Payment Reference', # 'Verwendungszweck'
    'Prima nota', # 'PrimaNota'
    'Remark', # 'Notiz'
    'Category', # 'Kategorien'
    'Type of Booking', # Transaktionstext
    'IBAN Empfänger', # no import
    'Empfängerkonto', # no import
    'BIC Empfänger', # no import
    'Bankleitzahl Empfängerbank', # no import
]

# read csv
d = pandas.read_csv('Pecunia.csv', delimiter=';', names=columns, index_col=False)

# fix amount format
d['Amount'] = d['Amount'].str.replace('.','')
d['Amount'] = d['Amount'].str.replace(',','.')

# create new columns 'Counter Account' and 'Counter Bank Code'
d['Counter Account'] = d['IBAN Empfänger'].combine_first(d['Empfängerkonto'])
d['Counter Bank Code'] = d['BIC Empfänger'].combine_first(d['Bankleitzahl Empfängerbank'])

# Export again:

d.to_csv('Hibiscus.csv',index=False, sep=';', quoting=csv.QUOTE_ALL)
