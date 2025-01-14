dist="$USERPROFILE/appdata/local/nvim"

if [ -d $dist ]; then
	echo "nvim folder already exists, do you wish to delete it? (yes/no)" 
	read confirmOnDelete	 
fi

 
if [ "$confirmOnDelete" == "yes" ]; then
    rm -r -f "$dist"
fi

[ -d $dist ] && echo "aborting.." && exit

echo "installing Neovim Config at $dist"

git clone https://github.com/Jalileh/nvimconf $dist
 
