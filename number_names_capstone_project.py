"""
program takes in a number and prints out the english word of that number.
works up to 99

"""


units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def num_to_words(num):

	if num == 0:
		return 'zero'

	if num >=1 and num <=19:
		return units[num]

	if num >= 20 and num <= 99:
		ten, remainder = divmod(num, 10)
		
		return tens[ten] + '-' + units[remainder]


print(num_to_words(54))


		





