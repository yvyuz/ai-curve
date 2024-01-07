import requests
import datetime
import xml.etree.ElementTree as ET

def get_arxiv_submissions(start_date, end_date, category='cs.AI', max_results_per_request=5000):
    query = f'cat:{category} AND submittedDate:[{start_date} TO {end_date}]'
    total_count = 0
    start = 0

    while True:
        url = f'http://export.arxiv.org/api/query?search_query={query}&start={start}&max_results={max_results_per_request}&exclude=abstract'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch data: HTTP Status Code {response.status_code}")
            break

        root = ET.fromstring(response.content)
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        count = len(entries)
        total_count += count

        if count < max_results_per_request:
            break

        start += count
    return total_count

def main():
    current_date = datetime.datetime.now()
    ten_years_ago = current_date - datetime.timedelta(days=10*365)

    # Adjust to start from the beginning of the month, ten years ago
    start_of_month = datetime.datetime(ten_years_ago.year, ten_years_ago.month, 1)
    while start_of_month < current_date:
        # Calculate the end of the month
        if start_of_month.month == 12:
            end_of_month = datetime.datetime(start_of_month.year + 1, 1, 1)
        else:
            end_of_month = datetime.datetime(start_of_month.year, start_of_month.month + 1, 1)
        end_of_month = end_of_month - datetime.timedelta(days=1)

        submissions = get_arxiv_submissions(start_of_month.strftime('%Y%m%d'), end_of_month.strftime('%Y%m%d'))
        print(f"{start_of_month.date()}, {submissions}")

        # Move to the next month
        start_of_month = end_of_month + datetime.timedelta(days=1)

if __name__ == "__main__":
    main()
