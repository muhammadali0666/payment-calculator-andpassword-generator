import urllib.request as urllib

print("This i site connectivity cheker program")

def main(url):
  print("Checking connectivity ")

  response = urllib.urlopen(url)
  print("Connected to ", url, "succesfully")
  print("the response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("input the url of the site you want to check: ")

main(input_url)