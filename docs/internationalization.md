# Internationalization

## How to add a language?

1\. Create a directory at the following location ``workalendar/locales/$YOURLANGUAGE``.

It is preferrable that your language code is of the form ``ll_CC``. That is to say that the language is lowercase, such as "fr", "pt", "en", while the country variant is uppercase ("FR" for France, "BR" for Brazil, "US" for the United States, etc).

2\. Run the following Makefile target:

```sh
$ make msginit
```

It's going to ask for your e-mail address, in order to mark you as the author of the translation file.

3\. Now your ``workalendar/locales/$YOURLANGUAGE/LC_MESSAGES/workalendar.po`` file is ready, you can now edit it using your tool of choice, a text editor or POEdit, which is a GUI for ``.po`` files.

Once you have translated from the source strings to the targets (partially or completely), you can check if you don't have errors by running the following Makefile target:

```sh
$ make compilemessages
```

If everything's fine, it should generate a `workalendar.mo` file besides your `workalendar.po` file.


## How to update a language file?

If the ``workalendar.po`` file previously generated is not up-to-date with the `workalendar.pot` template, you can update it using the following Makefile target:

```sh
$ make msgmerge
```

This command will merge (as cleverly as possible) the existing ``.po`` file and the updated ``.pot``, without erasing the previous translations.

You will now be able to edit the file as seen in the step 3 of the *"How to add a language?"* section.

## I've added a translatable string, now what?

If you've added or changed or removed a translatable string, you may want to make sure that all the available language files are updated.

This target updates the ``workalendar.pot`` file:

```sh
make makemessages
```

As seen in the section above, you may want to run the following to upgrade the `.po` files so they would include the changes.

```sh
make msgmerge
```

Then again, use the appropriate tools to edit your translations and compile them so you'd have access to the translated strings.
