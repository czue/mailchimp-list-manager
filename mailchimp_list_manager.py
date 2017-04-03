#!/usr/bin/env python
from __future__ import print_function
from mailchimp3 import MailChimp
import config


def main():
    client = MailChimp(config.MAILCHIMP_USERNAME, config.MAILCHIMP_SECRET_KEY)
    pending_members = _get_pending_members(client, config.LIST_ID)
    if pending_members:
        to_delete = []
        to_subscribe = []
        if raw_input("found {} pending members. process these now? (Y/n) ".format(
                len(pending_members))).lower() != 'n':
            for member in pending_members:
                todo = raw_input("{}: (d)elete, (s)ubscribe, do (n)othing, (p)rocess updates and exit? (d/s/N/p) ".format(
                    member['email_address']
                )).lower()
                if todo == 'd':
                    to_delete.append(member['id'])
                    print('{} tagged for deletion'.format(member['email_address']))
                elif todo == 's':
                    to_subscribe.append(member['id'])
                    print('{} tagged for subscription'.format(member['email_address']))
                elif todo == 'p':
                    print('processing updates and exiting...')
                    break
                else:
                    print('doing nothing')

            if to_delete:
                if raw_input("deleting {} members. this can't be undone! proceed? (y/N) ".format(
                        len(to_delete))).lower() == 'y':
                    for user_id in to_delete:
                        client.lists.members.delete(config.LIST_ID, subscriber_hash=user_id)
                    print('{} members deleted'.format(len(to_delete)))
            if to_subscribe:
                if raw_input("subscribe {} members? (Y/n) ".format(
                        len(to_subscribe))).lower() != 'n':
                    for user_id in to_subscribe:
                        client.lists.members.update(config.LIST_ID, subscriber_hash=user_id, data={"status": "subscribed"})
                    print('{} members subscribed!'.format(len(to_subscribe)))
    else:
        print("You don't have any pending list members. Congrats!")


def _get_pending_members(client, list_id):
    return client.lists.members.all(list_id, get_all=True, status='pending')['members']


if __name__ == "__main__":
    main()
