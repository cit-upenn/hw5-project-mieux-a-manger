import ast
import json
import WordCloudGenerator

'''
This file helps build the JSON and word cloud images for the final web page to display
'''


def format_file_for_web(resutls_file):
    """
    This is a helper function designed very specifically for our rank_outcome results.
    The results are shown as what a dictionary would look like per line.
    So we will use helper to format them into the final json.
    :param resutls_file: result file for top 5 of all cuisines
    """
    out = []  # final output list - a 2d array
    counter = 0
    maximum = 0

    with open(resutls_file, "r") as fin:
        for line in fin:
            counter += 1
            if counter > 5:
                counter = 1

            # parse the file into dict
            parsed = ast.literal_eval(line.rstrip())
            if counter == 1:
                maximum = float(parsed['rank_score'])

            # per business, we will represent it as a list of cuisine, rank, name, score (rounded)
            temp_line = []
            temp_line.append(parsed['category'])
            temp_line.append(str(counter))
            temp_line.append(parsed['name'])
            temp_line.append(parsed['category'] + str(counter) + ".png")
            temp_line.append(str(round(float(parsed['rank_score']) / maximum * 100 - 1, 0)))
            temp_line.append(parsed["business_id"])

            # each line = [['category', 'rank', 'name', 'picture_addr', 'score', 'business_id']
            out.append(temp_line)

    return out


def write_formatted_list_to_json_str(formatted_list):
    """
    Pretty write the json file. This helper is similar but a bit different from the one in FileParser
    :param formatted_list: output of format_file_for_web: 2d list of lists with items to write.
            each line in the list: [['category', 'rank', 'name', 'picture_addr', 'score', 'busines_id']
            but here we do not use business id
    """
    '["foo", {"bar":["baz", null, 1.0, 2]}]'
    temp_json_str = '{\n'
    category = 'none'
    counter = 0

    for line_list in formatted_list:
        counter += 1

        # new category to write
        if line_list[0].lower() != category:
            if counter != 1:
                temp_json_str += "], \n"

            category = line_list[0].lower()
            temp_json_str += "\t\"" + category + "\"" + ": [{\n"

        else:
            temp_json_str += ",{\n"

        temp_json_str += "\t\t" + '"rank": ' + line_list[1] + ", \n"
        temp_json_str += "\t\t" + '"name": "' + line_list[2] + "\", \n"
        temp_json_str += "\t\t" + '"keywords": "' + line_list[3] + "\", \n"
        temp_json_str += "\t\t" + '"score": ' + line_list[4] + "\n"
        temp_json_str += "\t}"

    temp_json_str += ']\n}\n'

    return temp_json_str


def build_json(results_file="datasets/rank_outcome.json", output_addr="test.json"):
    """
    Putting everything together and output the json file
    :param results_file: results file to get data from
    :param output_addr: where to store the output
    """
    formatted_list = format_file_for_web(results_file)
    json_str = write_formatted_list_to_json_str(formatted_list)

    with open(output_addr, "w") as fout:
        fout.write(json_str)


def build_word_cloud(results_file="datasets/rank_outcome.json", output_dir="web/"):
    """
    Make the word cloud jpg files into directed folder based on given results
    :param results_file: json final ranking results file to get data from
    :param output_dir: directory to store the jpg
    """
    formatted_list = format_file_for_web(results_file)
    for business in formatted_list:
        # note the 6th item is the business id
        destination = output_dir + business[3]  # file address = director + filename
        WordCloudGenerator.generate_wordcloud(business[5], destination)


if __name__ == '__main__':
    # build_json("web/reviews.json")
    # build_word_cloud()
    print "done"
