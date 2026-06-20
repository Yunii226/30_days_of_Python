#1
lst = list()

#2
mobiles=["Google", "Apple", "Xiaomi", "Samsung", "Nothing", "Nokia"]

#3
print(len(mobiles))

#4
print(mobiles[0], mobiles[(len(mobiles)-1)//2], mobiles[-1])

#5
mixed_data_types=["Unai", 21, 1.76, "Single", "Villasequilla"]

#6
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print (it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0], it_companies[(len(it_companies)-1)//2], it_companies[-1])

#10
it_companies[3]="NVIDIA"
print(it_companies)

#11
it_companies.append("Anthropic")

#12
it_companies.insert((len(it_companies)-1)//2,"OpenAI")
print(it_companies)

#13
it_companies[2]=it_companies[2].upper()
print(it_companies)

#14
it_companies.extend("#; ")
print(it_companies)

#15
print("Google" in it_companies)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19
print(it_companies[-4:-1])

#20
print(it_companies[(len(it_companies)-1)//2])

#21
it_companies.remove(it_companies[0])

#22
it_companies.remove(it_companies[(len(it_companies)-1)//2])

#23
it_companies.remove(it_companies[-1])

#24
it_companies.clear()

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = (front_end+back_end).copy()

#27
full_stack.insert(full_stack.index("Redux"),"Python")
full_stack.insert(full_stack.index("Redux"),"SQL")
print(full_stack)
 
#LEVEL 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
max_age=ages[-1]
min_age=ages[0]
ages.append(max_age)
ages.append(min_age)

print("Median", ages[(len(ages)-1)//2]/2)
average= sum(ages)/len(ages)
print(f"Range: {max_age-min_age}")
print(f"{min_age}-{average} == {max_age}-{average}: {abs(min_age-average)==abs(max_age-average)}")

#2
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(countries[(len(countries)-1)//2])

countries_1 = countries[0:(len(countries)//2)+1]
countries_2 = countries[(len(countries)//2)+1:-1]

print("Countries 1: ",countries_1)
print("Countries 2: ",countries_2)

#3
small_countries_list= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = small_countries_list

print(china)
print(russia)
print(usa)
print(scandic)