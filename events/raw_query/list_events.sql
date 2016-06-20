SELECT
	e.*, count(l.id) AS count_like,
	count(DISTINCT p.user_id) as count_participant,
	u.full_name AS owner_name,
	u.id as owner_id,
	u.avatar_id as owner_avatar_id,
	ch.name AS channel_name,
	ch.id as channel_id
FROM
	event_tab AS e
LEFT JOIN like_tab AS l ON l.event_id = e.id
LEFT JOIN participant_tab as p on p.event_id = e.id
INNER JOIN user_account_tab AS u ON u.id = e.creator_id
INNER JOIN channel_tab AS ch ON ch.id = e.channel_id
Where 1 = 1

