open('onion_headlines_filtered.txt','w', encoding = "utf-8").writelines(line for line in open('onion_headlines.csv', encoding = "utf-8") if ',1' in line)