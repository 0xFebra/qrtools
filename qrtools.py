import argparse
import qrcode

parser = argparse.ArgumentParser(description="QR Code Generator")

#declare arguments
parser.add_argument('-g','--generate',type=str,help='Generate QR Code',required=True)
parser.add_argument('-o','--output',type=str,help='Default QR Ouput Name : \"ScanMe\"',required=False)
args = parser.parse_args()

def qr_generate(generate,output):
    qr = qrcode.make(generate)
    if output is not None:
        qr.save(output + ".png")
    else:
        qr.save('ScanMe.png')
def main():
    qr_generate(args.generate,args.output)
main()
