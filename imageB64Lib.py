import base64
import os

#these are where you make your functions
#TODO replace all filenames and variable with src and targets


def encode_image_to_b64(src,target):
	"""
	1. open it as binary
	2. encode in b64
	3. print to a new file
	remove pass when you're ready to test it
	Figure out more about what src does/how to use it
	"""
	#imagefile = 'tron.jpg'
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(src, 'rb') as bytesimage:
		image = bytesimage.read()

	b64image = base64.b64encode(image)

	cipher_bytes = bytearray(b64image)
	#ofname = 'b64tron.enc'

	with open(target,'wb') as outfile:
	    outfile.write(cipher_bytes)
	print(cipher_bytes)

	#pass

def decode_image_from_b64(src,target):
	"""
	1. Open it as read
	2. Find decode from b64
	3. Decode from utf-8
	4. save to a new file
	"""
	#dir_path = os.path.dirname(os.path.realpath(__file__))

#filename = 'b64.tron.enc'
	with open(src, 'r') as image_encrypted:
		ciphertext= image_encrypted.read()

	cipherbytes = base64.b64decode(ciphertext)


#new_filename = 'tron_3.jpg'

	with open(target, 'wb') as decrypted_file:
		decrypted_file.write(cipherbytes)

		#what is the problem here? ^^^
	#pass

def compare_image_files(src1,src2):
	"""
	1. Open one as as bytes
	2. Open the second as bytes
	3. Compare them
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))


#imagefile = 'tron.jpg'
	with open(src1, 'rb') as bytesimage:
		image_1 = bytesimage.read()
		print(image_1)

#imagefile_2 = 'tron2a.jpg'
	with open(src2, 'rb') as bytesimage_2:
		image_2 = bytesimage_2.read()
		print(image_2)

		if image_1 == image_2:
			print('These images are the same')

		else:
			print('These images are different')
		#pass
