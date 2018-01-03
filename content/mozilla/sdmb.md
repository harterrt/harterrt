title: Managing Someday-Maybe Projects with a CLI
slug: sdmb
date: 2018-01-03

I have a problem managing projects I'm interested in but don't have time for.
For example, the [CLI for generating slack alerts] I posted about last year.
Not really a priority, but helpful and not that complicated.
I sat on that project for about a year before I could finally execute on it.

I want to be able to keep track of these projects for inspiration,
but **my TODO list get's overwhelming**
if I try to include all of these low-priority projects.
Getting Things Done suggests keeping a "Someday-Maybe (SDMB)" folder
that you review regularly.
I tried this, but even the SDMB list gets unweildy so I dread reviewing it.

I think I have a handle on it now, though <sup>1</sup>.
I started a directory at `~/sdmb`
with markdown files for each SDMB project.
This is nice for two reasons:

1. It doesn't clog up your task list with un-actionable tasks
2. You can review a list of SDMB *projects*
   without reviewing all of the associated *TODOs*.
   The **project list should be much shorter** and
   I can usually tell what's interesting by reviewing the project names.
   I don't need to know the next action.

Here's a bash snippet to make this feel natural.
It creates a new command `sdmb` that either
lists all projects in the SDMB folder
or opens a given SDMB project file (with auto-complete!).

I recommend reviewing the list of projects monthly.
If any projects look interesting,
review that project's notes and pull out a couple of TODOs.

Here's the snippet:
```bash
dir="$HOME/somedaymaybe"

_list_sdmb_projects () {
    ls -1 $dir | cut -f 1 -d '.'
}
    
sdmb () {
    if [ $# -eq 0 ]
    then
        # If no arguement provided, list available projects
        _list_sdmb_projects 
    else
        # Edit given project
        local id="$1"
        local file="$dir/$id.md"

        vim "$file"
    fi
}

# Bash auto-complete
_sdmbComplete()
{
	local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "$(_list_sdmb_projects)" -- $cur ))
}

complete -F _sdmbComplete sdmb
```

---

<sup>1</sup>: Thanks to Tom's great post [here][inspiration] for inspiration:

[CLI for generating slack alerts]: /slack_alerts.html
[inspiration]: https://cs-syd.eu/posts/2016-02-21-return-to-taskwarrior
