# Code Base Overview

## Chrome scripts

### Chrome Profiles

-   json config

    -   defines chrome profile path template
    -   defines computers

-   get_chrome_profile
    -   loads config
    -   checks profile exists
    -   returns profile data

### Chrome Automation

-   open_chrome_with_profile
    -   checks valid url
    -   gets chrome profile
    -   sets chrome options
    -   lunches browser
    -   returns driver

## Utils

### Json Utils

-   convert_paths_to_json_safe
    -   converts paths in json string to forward slash /
-   append_json_strings_to_array
    -   appends json string or list of them to file

## Chatgpt Automation

### Chatgpt Automation

-   send_prompt

    -   sends prompt as a one line string

-   send_multiline_prompt

    -   sends prompt by typing each line stacking them with shift + enter

-   save_response

    -   saves last chatgpt response in markdown file

-   save_code_block
    -   appends last chatgpt response, that is code block, to json/md/txt file

### Chatgpt CLI

-   open_chatgpt_session

    -   opens chatgpt, waits x seconds

-   send_chatgpt_prompt

    -   sends prompt with multiline method, waits x seconds

-   save_chatgpt_code_block
    -   saves last response code block, waits x seconds

## Archive

-   TaskPrompt
    -   fetches task form api
    -   generates prompt
-   CodeAgent
    -   use ChatGPTAgent
    -   sends TaskPrompt prompt

## Agents

-   ChatGPTAgent
    -   class with ability to:
        -   send_prompt
        -   save_code
-   CodeBaseAgent
    -   agent with ability to process path with py code and produce metadata about it
