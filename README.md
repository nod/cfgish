
```
       __       _     _
  ___ / _| __ _(_)___| |__
 / __| |_ / _` | / __| '_ \
| (__|  _| (_| | \__ \ | | |
 \___|_|  \__, |_|___/_| |_|
          |___/
```

# easier configs

After writing the same configuration logic across dozens of projects, I realized
that's not very DRY of me.

aka - simple wrapper around python's builtin configparser

## possible questions

> Why ini files?

They work pretty well, fairly robust. Interpolation works. Complex
configurations probably need more than this library anyway.

> Why not YAML,JavaScript, TOML, BLARGSNARFLE,....?

see above, "Why ini files?"

## usage

Given a sample config of:

```
blech: blippy


[section]
hi: there
```

You can use cfgish in your code to simplify reading from that file.

```python
import cfgish

cfg = cfgish.Configurator('~/.mycfg')

# get a value
cfg.get('blech') # returns 'blippy'
cfg.get('section:hi') # sugar to get into sections easier, return 'there'
```

### environment fallback

It is also possible to read from the environment at runtime.

if you set `CFG_SOME_VAL=blah` in your environment, in python you could access it
as:

```python
cfg.get('some_val') # returns blah
```

## requirements

python 3.4+

## developing

Use the Makefile

**setup your dev environment** - `make devlocal`

**run tests** - `make test`


