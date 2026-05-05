import pandas

emails = pandas.read_csv("emails.csv")

def process_email(text):
    text = text.lower()
    return list(set(text.split( )))

emails['words'] = emails['text'].apply(process_email)
sum(emails['spam'])/len(emails)

model = {}

for index, row in emails.iterrows():
    print(row)
    for word in row['words']:
        if word not in model:
            model[word] = {'spam' : 1, 'ham': 1}
        if word in model:
            if row['spam']:
                model[word]['spam'] += 1
            else: 
                model[word]['ham'] += 1 
