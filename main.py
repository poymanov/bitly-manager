import bitlink
import argparse


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Managing urls via bit.ly: create short links and clicks statistics')
	parser.add_argument('url')
	args = parser.parse_args()
	result = bitlink.process_url(args.url)

	if result is None:
		print('Something went wrong')
	else:
		print(result)