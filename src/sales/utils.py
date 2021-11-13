import uuid, base64
from profiles.models import Profile
from customers.models import Customer
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

def generate_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_key(res_by):
    if res_by == '#1':
        key = 'transaction_id'
    elif res_by == '#2':
        key = 'created'
    else:
        key = 'No data'
    return key

def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    key = get_key(results_by)
    print(key)
    print(data)
    data = data.groupby(key, as_index=False)['total_price'].agg('sum')
    if chart_type == '#1':
        print('bar chart')
        # plt.bar(data['transaction_id'], data['price'])
        sns.barplot(x=key, y='total_price', data=data)
    elif chart_type == '#2':
        print('pie chart')
        plt.pie(data=data, x= 'total_price', labels=data[key].values)
    elif chart_type == '#3':
        print('Line chart')
        plt.plot(data['transaction_id'], data['total_price'], color='blue',marker='o' )
    else:
        print('ups. ..... wrong chart type')
    
    plt.tight_layout()
    chart = get_graph()
    return chart