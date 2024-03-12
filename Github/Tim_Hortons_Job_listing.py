import requests
import pandas as pd


def get_jobs(lat=None, long=None, results=20):
    if lat is None or long is None:
        raise ValueError("Both Longitude and Latitude must be provided")

    base_url = f"https://api.higherme.com/classic/jobs"

    params = {
        'page': 1,
        'includes': 'location,location.company,location.externalServiceReferences',
        'limit': results,
        'filters[brand.id]': '58bd9e7f472bd',
        'filters[lat]': lat,
        'filters[lng]': long,
        'filters[distance]': 20,
        'sort[distance]': 'asc'
    }

    headers = {
        'authority': 'api.higherme.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'higherme-client-version': '2024.02.28_8.0',
        'origin': 'https://app.higherme.com',
        # 'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        # 'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    response_data = get_jobs(43.6447708,-79.37330639999999, results=60)
    if response_data:
        data2 = pd.DataFrame(data=[r.get('attributes') for r in response_data.get('data')],
                             columns=['title', 'summary_no_html', 'about', 'requirements', 'salary', 'full_time',
                                      'part_time'])
        print(data2)
        data2.to_excel('Tim_Hortons_Job.xlsx')


if __name__=="__main__":
    main()

