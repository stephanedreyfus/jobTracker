/** Classes for creating a jobs list and individual jobs. */

const BASE_URL = "http://localhost:5000"

class JobList {
  constructor(jobs) {
      this.jobs = jobs;
  }

  static async getStories() {
    const resp = await axios.get(`${BASE_URL}/jobs`);
    const jobs = resp.data.jobs.map(job => new Job(job));

    const joblist = new JobList(jobs);
    return joblist;
  }
}