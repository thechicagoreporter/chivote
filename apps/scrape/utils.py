import requests, json
from apps.candidates.models import Candidate
from apps.races.models import Race
from chivote.settings.base import BASE_DIR

### START CONFIG ###
scrape_target = 'https://chicagoelections.com/results/ap/summary.txt'
data_line_range_start, data_line_range_end = 3, 181
race_code_range_start, race_code_range_end = 0, 4
cand_code_range_start, cand_code_range_end = 0, 7
race_name_range_start, race_name_range_end = 32, 87
cand_name_range_start, cand_name_range_end = 88, 126
lookup_json_path = BASE_DIR + '/apps/scrape/lookup.json'
### END CONFIG ###


def get_page():
    return requests.get(scrape_target).content.decode()


def get_data(page=get_page()):
    return page.splitlines()[data_line_range_start:data_line_range_end]


def get_race_code(line):
    race_code = line[race_code_range_start:race_code_range_end]
    return race_code


def get_cand_code(line):
    return line[cand_code_range_start:cand_code_range_end]


def get_cand_name(line):
    return line[cand_name_range_start:cand_name_range_end].strip()


def get_race_name(line):
    return line[race_name_range_start:race_name_range_end].strip()


def make_lookup_json(data=get_data()):
    """
    use scraped cboe_results_id
    to look up chi.vote name
    and also sanity check cboe_results_name
    {cboe_results_id:
        {
        'chi_vote_name':'XXXXX',
        'cboe_results_name':'YYYYYY'
        },
    }
    """
    lookup = {'races':dict(),'candidates':dict()}
    for line in get_data():
        # add candidates
        cboe_cand_results_code = get_cand_code(line)
        cboe_cand_results_name = get_cand_name(line)
        try:
            candidate = Candidate.objects.get(cboe_results_id=cboe_cand_results_code)
        except Exception as e:
            print(e)
            import ipdb; ipdb.set_trace()
        lookup['candidates'][cboe_cand_results_code] = {
                'chi_vote_name':candidate.full_name,
                'cboe_results_name':cboe_cand_results_name,
                }

        # add races, if not added already
        cboe_race_results_code = get_race_code(line)
        if cboe_race_results_code in lookup['races']:
            continue
        cboe_race_results_name = get_race_name(line)
        race = Race.objects.get(cboe_results_id=cboe_race_results_code)
 
        lookup['races'][cboe_race_results_code] = {
                'chi_vote_name':race.results_slug,
                'cboe_results_name':cboe_race_results_name,
                }
        
        # write out
        lookup_file = open(lookup_json_path,'w')
        json.dump(lookup,lookup_file)
        lookup_file.close()
