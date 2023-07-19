from train import *
from arguments import Arguments

args = Arguments().parser().parse_args()

args.device = torch.device('cuda:'+ str(args.gpu) if torch.cuda.is_available() else 'cpu')
torch.cuda.set_device(args.device)

model = GAN(args)
model.run()