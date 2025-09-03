import requests

def checking(url):
    try:
        reponse = requests.get(url, timeout=5)
        if reponse.status_code == 200:
            return f"{url} is online."
        else:
            return f"{url} returned status code : {reponse.status_code}."
    except:
        return f"{url} is unreachable."
 
def main():
    filename = input("Enter the name of the text file with website URLs (e.g., websites.txt): ")
    try:
        with open(filename, 'r') as file:
            websites = []
            for line in file:
                if line.strip():
                    websites.append(line.strip())
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. please check the file name and try again.")
    
    results = []
    
    for site in websites:
        status = checking(site)
        print(status)
        results.append(status)
        report_file = "status_report.txt"
        with open(report_file, 'w') as report:
            report.write("\n".join(results))
    print(f"\nResults saved to '{report_file}'.")

if __name__ == "__main__":
    main()