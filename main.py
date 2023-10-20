from train import *
from arguments import Arguments

import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1" 

args = Arguments().parser().parse_args()

args.device = torch.device('cuda:'+ str(args.gpu) if torch.cuda.is_available() else 'cpu')
#torch.cuda.set_device(args.device)

model = GAN(args)
model.run()