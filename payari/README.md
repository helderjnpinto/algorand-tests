# Development

```bash
algokit localnet start
```

> Setup envs in .env.example to .env with sandbox accounts and tokens.

## Dev contracts

```bash
watchexec -w ./contracts 'tealish compile ./contracts/payari.tl'
```

## Testing

```bash
watchexec -w ./test 'make test'
```

### Running specific test

manually change the makefile

```bash
watchexec -w ./test 'make specific_test'
```

## Static analyzer

TODO: check tealer tool

- https://github.com/crytic/tealer
