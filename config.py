import http.client

conn = http.client.HTTPSConnection("facebook-pages-scraper2.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "6bbf527987msh805263045201c3bp196394jsn709dd888d6b7",
    'x-rapidapi-host': "facebook-pages-scraper2.p.rapidapi.com"
}

conn.request("GET", "/get_facebook_reels_details?link=https%3A%2F%2Fwww.facebook.com%2Fmancity", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
