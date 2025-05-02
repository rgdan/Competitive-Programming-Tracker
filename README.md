![Image](images/logos.jpg)

# Competitive Programming Tracker

This tool reads a CSV file with usernames for **AtCoder**, **CodeChef**, **CodeForces**, and **OmegaUp**, fetches how many problems each user has solved, and outputs a clean `.txt` summary.

## Why This Exists

In a university course, students were assigned problems to solve across four competitive programming platforms. The number of problems solved was part of their grade.

This script automates the task of checking each platform manually, making grading easier and faster.

## I/O

### Input

You need a .csv file that contains one row per student, with their usernames on each platform.

#### Example Format

```csv
Name,AtCoder,CodeChef,CodeForces,Omegaup
Henry,at_snek,chef_l33t,cf_overflow,omega_void
William,at_rainbow,chef_9000,cf_dreams,omega_whirl
```
### Output

It'll output a `.txt` file named `results.txt` in the same directory as the script.

#### Example Format

```txt
Name            | AtCoder | CodeChef | CodeForces | AC+CC+CF | Omegaup
-----------------------------------------------------------------------
Henry           | 10      | 12       | 13         | 35       | 80
William         | 5       | 7        | 10         | 22       | 49
```

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
