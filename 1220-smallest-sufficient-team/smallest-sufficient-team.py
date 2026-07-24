class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)

        # skill -> bit
        skill_id = {s: i for i, s in enumerate(req_skills)}

        # mask for each person
        person_masks = []
        for skills in people:
            mask = 0
            for s in skills:
                mask |= 1 << skill_id[s]
            person_masks.append(mask)

        FULL = (1 << m) - 1

        # dp[mask] = smallest team achieving mask
        dp = {0: []}

        for i, pmask in enumerate(person_masks):
            # snapshot because dp changes during iteration
            for mask, team in list(dp.items()):
                new_mask = mask | pmask
                if new_mask == mask:
                    continue

                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

        return dp[FULL]