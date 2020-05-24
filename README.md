1. Make Folder in Documents Folder called Dev. 
2. Insall Git from https://git-scm.com/download/win
3. Download https://github.com/igmec/igmec as a ZIP
4. Extract into Documents/Dev/igmec
5. Run igmec/Configs/Scripts/copyConfigs.bat (Make sure the Directory matches, eg. Igor vs Igor M)
6. Generate a new SSH key for practice/igmec account using Git Bash: https://help.github.com/en/enterprise/2.17/user/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
	$ ssh-keygen -t rsa -b 4096 -C "igor_mech@hotmail.com"
	/c/Users/Igor M/.ssh/id_rsa_practice
	blackdiamondstring as pass
7. Add practice SSH Key to ssh-agent
	$ eval $(ssh-agent -s)
	$ ssh-add ~/.ssh/id_rsa_practice
8. Add the SSH Key to practice igor_mech@hotmail.com Github account: https://help.github.com/en/enterprise/2.17/user/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account
	$ clip < ~/.ssh/id_rsa_practice.pub
	Github account > Settings > SSH and GPG Keys > New/Add SSH Key
	Title: Name for Computer
	Paste Key > Add SSH Key
	Confirm with password
9. Test SSH connection
	$ ssh -T git@practice
	yes
	blackdiamondstring
10. Repeat steps 6-9 for main/igormec account, use deafult id_rsa for it

	
