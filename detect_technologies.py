import argparse
import requests
import re
from colorama import Fore, Style, init

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

# Categories of web technologies
CATEGORIES = {
    "CMSs": ["WordPress", "Joomla", "Drupal", "Magento", "Ghost", "Concrete5", "TYPO3", "Grav", "DotNetNuke", "Umbraco",
             "Craft CMS", "HubSpot CMS", "Squarespace", "Wix", "Shopify"],
    "Web Development Frameworks": ["Angular", "React", "Vue.js", "Svelte", "Ember.js", "Backbone.js", "Laravel",
                                    "Symfony", "CodeIgniter", "CakePHP", "Django", "Flask", "Express.js", "Spring Boot",
                                    "Ruby on Rails", "ASP.NET", "Koa", "Phoenix"],
    "Web Servers": ["Apache", "Nginx", "LiteSpeed", "IIS", "Caddy", "Hiawatha", "Cherokee"],
    "Application Servers": ["Tomcat", "JBoss", "GlassFish", "WebSphere", "WebLogic", "Jetty"],
    "Programming Languages": ["PHP", "Python", "Java", "Ruby", "JavaScript", "TypeScript", "Go", "C#", "Scala", "Perl",
                               "C++"],
    "Database Systems": ["MySQL", "PostgreSQL", "MongoDB", "MariaDB", "Oracle Database", "Microsoft SQL Server",
                         "SQLite", "CouchDB", "Cassandra", "Redis"],
    "DevOps Tools": ["Jenkins", "GitLab CI/CD", "CircleCI", "Bamboo", "Ansible", "Terraform", "Docker", "Kubernetes"],
    "Monitoring and Logging": ["Splunk", "ELK Stack", "Prometheus", "Grafana", "Zabbix", "Datadog", "Nagios", "New Relic"],
    "E-commerce Platforms": ["WooCommerce", "PrestaShop", "OpenCart", "BigCommerce", "Salesforce Commerce Cloud"]
}

def detect_technologies(content):
    """Detect technologies in a given content string."""
    detected = {category: [] for category in CATEGORIES}
    for category, tech_list in CATEGORIES.items():
        for tech in tech_list:
            if re.search(r'\b' + re.escape(tech) + r'\b', content, re.IGNORECASE):
                detected[category].append(tech)
    return {cat: techs for cat, techs in detected.items() if techs}

def process_url(url, scan_all=False):
    """Process a single URL to detect technologies."""
    try:
        # Fetch the response but do not raise for status
        response = requests.get(url, timeout=10, allow_redirects=True)
        
        # Combine headers, cookies, and content if --all is used
        detected_technologies = {}
        if scan_all:
            headers_content = ' '.join(f"{key}: {value}" for key, value in response.headers.items())
            cookies_content = ' '.join(f"{key}: {value}" for key, value in response.cookies.items())
            combined_content = f"{headers_content}\n{cookies_content}\n{response.text}"
            detected_technologies = detect_technologies(combined_content)
        else:
            detected_technologies = detect_technologies(response.text)

        return detected_technologies
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(description="Detect technologies/frameworks used by websites.")
    parser.add_argument('-u', '--url', type=str, help="Single URL to scan.")
    parser.add_argument('-f', '--file', type=str, help="File containing list of URLs to scan.")
    parser.add_argument('--all', action='store_true', help="Scan headers, cookies, and HTML content for technologies.")
    args = parser.parse_args()

    if not args.url and not args.file:
        parser.print_help()
        exit(1)

    urls = []
    if args.url:
        urls.append(args.url)
    if args.file:
        try:
            with open(args.file, 'r') as file:
                urls.extend(line.strip() for line in file if line.strip())
        except FileNotFoundError:
            print(f"File not found: {args.file}")
            exit(1)

    for url in urls:
        print(f"Scanning {url}...")
        technologies = process_url(url, scan_all=args.all)
        if technologies:
            print(f"Technologies detected on {url}:")
            for category, tech_list in technologies.items():
                colored_category = f"{Fore.GREEN}{category}{Style.RESET_ALL}"
                colored_techs = ', '.join(f"{Fore.RED}{tech}{Style.RESET_ALL}" for tech in tech_list)
                print(f"  {colored_category}: {colored_techs}")
        else:
            print(f"No technologies detected on {url}.")

if __name__ == '__main__':
    main()
