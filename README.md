Some Templates

# RMarkdown with hebrew support and Chicago+ibid setup in Neovim

In the vimrc I use :


```
func! ToggleHebrew()
	if &rl
		set norl
       		set keymap=
	else
		set rl
		set keymap=hebrew
	end
endfunc
```


another option in Linux is to use Bicon though it have issue with cancel all the bindings.

the style is taken from csl official git, i had some issues with employing both english and hebrew so i just translated the main line.

in order to start a new file in shell you can add the provisional script(probably can be improved by hard coding the path once it is deployed):

```
function NewRMD-H ()
{
	local FileName=$1
	cp [path to the template]/Default-Hebrew.rmd "./$FileName"

	cp [path to the template]/chicago-fullnote-bibliography-with-ibid.csl ./
	nvim $FileName
}
```
