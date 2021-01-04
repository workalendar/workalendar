# Advanced feature: class options

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [ISO Registry](iso-registry.md) / [iCal Export](ical.md) / [Contributing](contributing.md)


As of `v13.0.0` you can define *options* for your calendar.

## Options as "flags"

Let's consider the following calendar class:

```python
@iso_register('ZK')
class Zhraa(WesternCalendar):
    include_easter_monday = True
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 2, "King Birthday"),
    )

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)

        days.append(
            (Zhraa.get_nth_weekday_in_month(year, 6, MON),
            'Day of the Founder'),
        )
        return days
```

In our example, we'll add a special holiday. It's **not** an official holiday, but it **can** be taken as a non-working day, if your organization or your administration decides it becomes one.

For the sake of our use-case, let's say that the Zhraa Kingdom decides that January the 2nd can be considered as a day off in some special cases, for banks or schools, for example. Or at the discretion of your company.

As an integrator, if you need to implement this behaviour, you can decide to have a separate class which includes your extra day. This would fit your needs.

But what if your special organization decides to keep this day as a non-working day depending on a variable context? Let's say that it does not happen every year, or it's not in every city of the Kingdom, or not for all of your employees, etc. Using a dedicated class won't help you there.  
But **optional arguments** surely will!

Here's a slightly different version of our `Zhraa` class:


```python
@iso_register('ZK')
class Zhraa(WesternCalendar):
    include_easter_monday = True
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 2, "King Birthday"),
    )

    def __init__(self, include_january_2nd=False, **kwargs):
        super().__init__(**kwargs)
        self.include_january_2nd = include_january_2nd

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)

        days.append(
            (Zhraa.get_nth_weekday_in_month(year, 6, MON),
            'Day of the Founder'),
        )

        if self.include_january_2nd:
            days.append(
                (date(year, 1, 2), "January 2nd")
            )
        return days
```

In your *business-logic code*, you could then write:

```python
include_january_2nd = year == 2019 \
    and (employee_name == "Bob" or employee_location == "North")
calendar = Zhraa(include_january_2nd=include_january_2nd)
```

As a consequence, depending on the context required by your business-logic process, you can include or exclude January 2nd as a holiday.

## More than "flags"

Of course, **you are not limited to booleans** to activate/deactivate a holiday when you want to create options. Use strings, numbers, objects, or whatever suits your needs.

Here are some examples:

* A ``region`` argument: in some regions, it defines new holidays, exceptions on including or excluding other days, etc.
* A `number_of_days_after_new_year` as a variable number of days that are to be accounted as non-working days after New Year's day.
* A ``day_of_the_founder_label`` string variable to easily customize the *Day of the Founder* label, according to your liking.
* ... sky is the limit!

## Caveats

### Why not using derivative classes?

Again, for each of these options, you could define an inherited class of `Zhraa`. But as you have more and more option values and exceptions to your rules, you'd have to define a new class for each of these combinations.

If you only have a couple of exceptions to your rules, you may prefer ot have a dedicated class. If the number of combinations goes over a limit, opt for *options*.

### ERR_TOO_MANY_OPTIONS

**Beware!** Options are nice and will help you in many cases, but it's probably a bad idea to go on and add dozens of them to your class constructor. As a consequence, your runtime code would be more and more complex. You'd have hard time covering all of the combinations around their values and test them.

As in many other cases, your mileage may vary, but I doubt that you want to combine more than 5 of them.

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [ISO Registry](iso-registry.md) / [iCal Export](ical.md) / [Contributing](contributing.md)
