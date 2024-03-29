/*
 * jingle-session.h - Header for GabbleJingleSession
 * Copyright (C) 2008 Collabora Ltd.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifndef __JINGLE_SESSION_H__
#define __JINGLE_SESSION_H__

#include <glib-object.h>
#include <wocky/wocky.h>

#include "jingle-content.h"
#include "jingle-factory.h"
#include "jingle-types.h"

G_BEGIN_DECLS

typedef enum
{
  MODE_GOOGLE,
  MODE_JINGLE
} GabbleMediaSessionMode;

typedef struct _GabbleJingleSessionClass GabbleJingleSessionClass;

GType gabble_jingle_session_get_type (void);

/* TYPE MACROS */
#define GABBLE_TYPE_JINGLE_SESSION \
  (gabble_jingle_session_get_type ())
#define GABBLE_JINGLE_SESSION(obj) \
  (G_TYPE_CHECK_INSTANCE_CAST((obj), GABBLE_TYPE_JINGLE_SESSION, \
                              GabbleJingleSession))
#define GABBLE_JINGLE_SESSION_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_CAST((klass), GABBLE_TYPE_JINGLE_SESSION, \
                           GabbleJingleSessionClass))
#define GABBLE_IS_JINGLE_SESSION(obj) \
  (G_TYPE_CHECK_INSTANCE_TYPE((obj), GABBLE_TYPE_JINGLE_SESSION))
#define GABBLE_IS_JINGLE_SESSION_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_TYPE((klass), GABBLE_TYPE_JINGLE_SESSION))
#define GABBLE_JINGLE_SESSION_GET_CLASS(obj) \
  (G_TYPE_INSTANCE_GET_CLASS ((obj), GABBLE_TYPE_JINGLE_SESSION, \
                              GabbleJingleSessionClass))

struct _GabbleJingleSessionClass {
    GObjectClass parent_class;
};

typedef struct _GabbleJingleSessionPrivate GabbleJingleSessionPrivate;

struct _GabbleJingleSession {
    GObject parent;
    GabbleJingleSessionPrivate *priv;
};

GabbleJingleSession *gabble_jingle_session_new (
    GabbleJingleFactory *factory,
    WockyPorter *porter,
    const gchar *session_id,
    gboolean local_initiator,
    WockyContact *peer,
    JingleDialect dialect,
    gboolean local_hold);

const gchar * gabble_jingle_session_detect (WockyStanza *stanza,
    JingleAction *action, JingleDialect *dialect);
gboolean gabble_jingle_session_parse (GabbleJingleSession *sess,
    JingleAction action, WockyStanza *stanza, GError **error);
WockyStanza *gabble_jingle_session_new_message (GabbleJingleSession *sess,
    JingleAction action, WockyNode **sess_node);

void gabble_jingle_session_accept (GabbleJingleSession *sess);
gboolean gabble_jingle_session_terminate (GabbleJingleSession *sess,
    JingleReason reason,
    const gchar *text,
    GError **error);
void gabble_jingle_session_remove_content (GabbleJingleSession *sess,
    GabbleJingleContent *c);

GabbleJingleContent *
gabble_jingle_session_add_content (GabbleJingleSession *sess,
    JingleMediaType mtype,
    JingleContentSenders senders,
    const char *name,
    const gchar *content_ns,
    const gchar *transport_ns);

GType gabble_jingle_session_get_content_type (GabbleJingleSession *);
GList *gabble_jingle_session_get_contents (GabbleJingleSession *sess);
const gchar *gabble_jingle_session_get_peer_resource (
    GabbleJingleSession *sess);
const gchar *gabble_jingle_session_get_initiator (
    GabbleJingleSession *sess);
const gchar *gabble_jingle_session_get_sid (GabbleJingleSession *sess);
JingleDialect gabble_jingle_session_get_dialect (GabbleJingleSession *sess);

gboolean gabble_jingle_session_can_modify_contents (GabbleJingleSession *sess);
gboolean gabble_jingle_session_peer_has_cap (
    GabbleJingleSession *self,
    const gchar *cap_or_quirk);

void gabble_jingle_session_send (
    GabbleJingleSession *sess,
    WockyStanza *stanza);

void gabble_jingle_session_set_local_hold (GabbleJingleSession *sess,
    gboolean held);

gboolean gabble_jingle_session_get_remote_hold (GabbleJingleSession *sess);

gboolean gabble_jingle_session_get_remote_ringing (GabbleJingleSession *sess);

gboolean gabble_jingle_session_defines_action (GabbleJingleSession *sess,
    JingleAction action);

WockyContact *gabble_jingle_session_get_peer_contact (GabbleJingleSession *self);
const gchar *gabble_jingle_session_get_peer_jid (GabbleJingleSession *sess);

const gchar *gabble_jingle_session_get_reason_name (JingleReason reason);

GabbleJingleFactory *gabble_jingle_session_get_factory (GabbleJingleSession *self);
WockyPorter *gabble_jingle_session_get_porter (GabbleJingleSession *self);

#endif /* __JINGLE_SESSION_H__ */

