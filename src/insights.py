from src.jobs import read


def get_unique_job_types(path):

    dados = read(path)
    getUniqueJob = []
    for jobs in dados:
        if jobs["job_type"] not in getUniqueJob and jobs["job_type"][0] != "2":
            getUniqueJob.append(jobs["job_type"])
    return getUniqueJob


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    data = read(path)
    getUniqueIndustries = []
    # nomeei como 'ind'
    # pois o lint reclamava de
    #  tamanho de linha então diminui o nome da variável
    for ind in data:
        if ind['industry'] not in getUniqueIndustries:
            if ind['industry'] != "" and not ind["industry"].isnumeric():
                getUniqueIndustries.append(ind['industry'])
    return getUniqueIndustries


get_unique_industries("src/jobs.csv")


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    reader = read(path)
    s = [s["max_salary"].isnumeric() and int(s["max_salary"])for s in reader]
    return max(s)

    # chamei a variavel salary de ' s ', lint reclamando de tamanho de linha


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
