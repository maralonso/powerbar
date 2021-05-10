# powerbar

Just a few segments to use with powerline and build a simple i3wm statusbar

![image](https://user-images.githubusercontent.com/35178295/117691056-da8d4e00-b191-11eb-9ebc-3a85dad94041.png)


## Usage

Chenage your i3 config in order to use the `powerline-i3.py` bar.

```
bar {
    status_command python3 /usr/lib/python3.9/site-packages/powerline/bindings/i3/powerline-i3.py
}
```

Add an entry on your `~/.config/powerline/config.json` file for wm bar.

```
		"wm": {
			"colorscheme": "i3_dark",
			"theme": "default",
			"update_interval": 10,
				"continuation": "continuation"
		}
```


Add segments to the bar editing `~/.config/powerline/themes/wm/default.json`

```
{
	"segments": {
		"right": [
            {
                "function": "powerbar.segments.common.hostname",
                "before": "\uE0A2 "
            },     
            {
                "function": "powwerbar.segments.common.bluetooth",
                "powerline_symbol": "\uE0B0"
            },

            {
                "function": "powerbar.segments.common.network",
                "before": " "
            },
            {
                "function": "powerlinemem.mem_usage.mem_usage",
                "args": {
                "short": 0
            },
                "after": " "
            },
            {
                "function": "powerline.segments.common.sys.cpu_load_percent",
                "args": {
                    "format": "{0:.2f}%"
                },
                "after": " "
            },
            {
                "function": "powerline.segments.common.sys.system_load",
                "after": " "
            },
            {
                "function": "powerbar.segments.common.volume",
                "before": "\u266c "
            },
            {
                "function": "powerline.segments.common.sys.uptime",
                "after": " "
            },
            {
                "function": "powerbar.segments.common.temp",
                "after": " "
            },
            {
                "function": "powerline.segments.common.bat.battery",
                "after": " "
            },
			{
				"function": "powerline.segments.common.time.date",
                "args": {
                    "format": "%a %-d %b"
                }
			},
			{
				"function": "powerline.segments.common.time.date",
				"name": "time",
				"args": {
					"format": "%H:%M",
					"istime": true
				}
			}
		]
	}
}
```

Finally we need a colorshceme for new segments. Add `~/.config/powerline/colorschemes/wm/i3_dark.json` with something like this
```
{
  "name": "i3 Dark",
  "groups": {
    "background":                 { "fg": "white", "bg": "gray0", "attrs": [] },
    "background:divider":         { "fg": "gray5", "bg": "gray3", "attrs": [] },
    "date":                       { "fg": "black", "bg": "gray6", "attrs": [] },
    "time":                       { "fg": "black", "bg": "gray6", "attrs": ["bold"] },
    "time:divider":               { "fg": "gray6", "bg": "gray6", "attrs": [] },
    "uptime":                     { "fg": "gray9", "bg": "darkestpurple", "attrs": [] },
    "network_load":               { "fg": "gray8", "bg": "gray0", "attrs": [] },
    "network_load_gradient":      { "fg": "green_yellow_orange_red", "bg": "gray0", "attrs": [] },
    "network_load_sent_gradient": "network_load_gradient",
    "network_load_recv_gradient": "network_load_gradient",
    "network_load:divider":       "background:divider",
    "system_load":                { "fg": "white", "bg": "solarized:blue", "attrs": [] },
    "system_load:divider":        { "fg": "white", "bg": "solarized:blue", "attrs": [] },
    "system_load_gradient":       { "fg": "yellow_red", "bg": "gray3", "attrs": [] },
    "cpu_load_percent":           { "fg": "gray8", "bg": "solarized:blue", "attrs": [] },
    "cpu_load_percent:divider":   { "fg": "gray8", "bg": "solarized:blue", "attrs": [] },
    "cpu_load_percent_gradient":  { "fg": "yellow_red", "bg": "gray3", "attrs": ["bold"] },
    "battery":                    { "fg": "gray8", "bg": "green", "attrs": [] },
    "battery_gradient":           { "fg": "white_red", "bg": "green", "attrs": [] },
    "battery_full":               { "fg": "red", "bg": "green", "attrs": [] },
    "battery_empty":              { "fg": "white", "bg": "red", "attrs": [] },
    "mem_usage":                  { "fg": "gray10", "bg": "yellow", "attrs": [] },
    "mem_usage_gradient":         { "fg": "GREEN_Orange_red", "bg": "gold3", "attrs": [] },
    "temp":                       { "fg": "gray10", "bg": "darkorange", "attrs": [] },
    "network":                    { "fg": "gray1", "bg": "solarized:magenta", "attrs": [] },
    "hostname":                   { "fg": "black", "bg": "darkcyan", "attrs": ["bold"] },
    "volume":                     { "fg": "gray1", "bg": "khaki1", "attrs": [] },
    "bluetooth":                  { "fg": "gray0", "bg": "lightyellowgreen", "attrs": [] }
  }
}
```
