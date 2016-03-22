#### Instructions:

Given a the name of a file containing known page links and one or more page names, output a list of all pages that can be visited from the given pages.

##### Data Storage Format:
```
# filename.txt containing:
PageName -> PageName3 PageName4 Pagename5
PageName2 -> PageName PageName4 PageName6
...
```
Write a command-line program that would print out a list of all pages that can be visited given one or more `PageName` values. Include pages that would require following several links to reach. Exclude names of initial pages from output.

##### Sample Input:
```
solution sample_input.txt AffiliateSite AffiliateSite2
```
#####Sample Output:
```
['Homepage', 'Catalog', 'CompetitorHomepage', 'Basket', 'ContactUs', 'DailyDeals', 'Checkout', 'CustomerServiceSite']
```

