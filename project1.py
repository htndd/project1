import requests


def get_crypto_price(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto_id]['usd']
    else:
        return None

if __name__ == "__main__":
    crypto_list = ['bitcoin', 'ethereum']
    for crypto in crypto_list:
        price = get_crypto_price(crypto)
        if price:
            print(f'{crypto.capitalize()} 價格：${price}')
        else:
            print(f'無法取得 {crypto} 價格')