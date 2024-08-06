def create_node(data, head=None):
    return {'dta':data, 'nxt': head}

#print(create_node(23))

def append_node(data, head):
    if head == None:
        return create_node(data)
    temp = head
    while temp['nxt'] is not None:
        temp = temp['nxt']
    temp['nxt'] = {'dta': data, 'nxt': None}
    #temp['nxt] = create_node(data)
    return head

def prepend(data, head):
    return create_node(data, head)

def printll(head):
    if not head:
        print('')
    arr = []
    temp = head
    while temp is not None:
        arr.append(str(temp['dta']))
        temp = temp['nxt']
    print('->'.join(arr))

def delete_node(data, head):
    if not head:
        return None
    if head['dta'] == data:
        return head['nxt']
    
    temp = head
    while temp['nxt'] is not None:
        if temp['nxt']['dta'] != data:
            temp = temp['nxt']
        else:
            temp['nxt'] = temp['nxt']['nxt']
            break
    return head

#def search_node(data, head):
    
            
   

ll1 = None
for i in range(0, 20, 2):
    ll1 = append_node(i, ll1)

ll2 = None

printll(ll1)
printll(delete_node(2, ll1))
printll(delete_node(14, ll1))
printll(delete_node(13, ll1))
printll(delete_node(14, ll1))
printll(delete_node(18, ll1))

