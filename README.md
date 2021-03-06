# youtubethemes

Skip to content
This repository
Search
Pull requests
Issues
Gist
 @arrthur
 Sign out
 Unwatch 1
  Star 0
  Fork 0 arrthur/youtubethemes
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathyoutubethemes/documentation/the_challenge.txt
4d15359  26 days ago
 Arthur Oliveira Youtube themes project
0 contributors
RawBlameHistory     
34 lines (31 sloc)  1.7 KB
# Overview
A friend has a YouTube channel, and wants to understand which themes get more attention, so he can make more videos on them.

# Task
You'll create a simple Django app, with the following models:
- `Theme`: A theme that has a `name`.
- `Thumb`: A thumbs up or thumbs down on a video. It should have:
    - `is_positive`: Whether or not this is a positive thumb.
    - `time`: The time when the thumbs up or down was given.
    - `video`: The video referenced by this thumb.
- `Comment`: A comment on a video. It should have:
    - `is_positive`: Whether or not this is a positive comment.
    - `time`: The time when the comment was written.
    - `video`: The video referenced by this comment.
- `Video`: An uploaded video. It should have:
    - `title`: The title of the video.
    - `date_uploaded`: The date it was uploaded (and not the date it was created in the database, so most likely this will be a date in the past). **Make sure that videos that are more than 1 year old should not be added, as they are less relevant.**
    - `views` The amount of views the video received.
    - `themes`: A **list** of themes used on the video (multiple).

There should be a route `get_popular_themes` that returns the list of themes (`id` and `name`), ordered by their success on the channel.
For each theme, its score will be given by the sum of the scores of all videos that contain that theme.

And this is the function used to rank a video:
```
Score = views * TimeFactor * PositivityFactor
```
Where:
```
TimeFactor = max(0, 1 - (days_since_upload/365))
PositivityFactor = 0.7 * GoodComments + 0.3 * ThumbsUp
GoodComments = positive_comments/(positive_comments+negative_comments)
ThumbsUp = thumbs_up/(thumbs_up+thumbs_down)
```
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
